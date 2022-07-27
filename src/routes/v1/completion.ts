import { FastifyPluginAsync, FastifyRequest } from 'fastify';
import { getEstimatedPrice } from 'lib/openai/utils/prices';
import { apiKeyService, generationService, openaiService } from 'lib/services';
import { authApp } from 'lib/utils/auth';

const routes: FastifyPluginAsync = async (app) => {
  await authApp(app);

  app.get('/', {
    schema: {
      tags: ['completion'],
      summary: 'Get short title',
      description: 'Get short title for a given title',
      params: {
        type: 'object',
        properties: {
          title: {
            type: 'string',
            description: 'Title to get short title for',
          },
        },
      },
      response: {
        200: {
          type: 'object',
          properties: {
            shortTitle: {
              type: 'string',
              description: 'Short title for the given title',
            },
            estimatedPrice: {
              type: 'number',
              description: 'Estimated price of the summarization',
            },
            priceUnit: {
              type: 'string',
              description: 'Price unit',
            },
          },
        },
      },
    },
  }, async (req: FastifyRequest<{Querystring: {title: string}}>, res) => {
    const { title } = req.query;
    if (!title) res.code(400).send({ error: 'title is required' });

    // Return cached output if exist.
    const generation = await generationService.getGeneration(title);
    let shortTitle = generation?.output;
    console.log(shortTitle);

    // If not cached, create.
    if (!shortTitle) {
      const { error, data } = await openaiService.getCompletion(title);
      if (error) res.code(400).send(error);
      shortTitle = data?.completion || '';

      // Log completion.
      const authKey = req.headers.authorization?.split(' ')[1];
      const apiKey = await apiKeyService.getByKey(authKey ?? '');
      await generationService.logGeneration({ input: title, output: shortTitle, apiKeyId: apiKey?.id ?? '' });
    }

    // Get estimated price.
    const price = getEstimatedPrice(title, shortTitle);
    return { shortTitle, estimatedPrice: price, priceUnit: 'USD' };
  });
};

export default routes;
