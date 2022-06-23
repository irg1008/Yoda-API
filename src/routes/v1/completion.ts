import { FastifyPluginAsync, FastifyReply, FastifyRequest } from 'fastify';
import { openaiService } from 'lib/services';

const routes: FastifyPluginAsync = async (app) => {
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
          },
        },
      },
    },
  }, async (req: FastifyRequest<{Querystring: {title: string}}>, res) => {
    const { title } = req.query;
    if (!title) res.code(400).send({ error: 'title is required' });
    const { error, data } = await openaiService.getCompletion(title);
    if (error) res.code(400).send(error);
    return { shortTitle: data?.completion };
  });
};

export default routes;
