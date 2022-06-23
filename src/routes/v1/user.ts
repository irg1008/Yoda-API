import { FastifyPluginAsync, FastifyRequest } from 'fastify';
import { userService } from 'lib/services';
import { authApp } from 'lib/utils/auth';

const routes: FastifyPluginAsync = async (app, opts) => {
  await authApp(app);

  app.get('/', {
    schema: {
      description: 'Get all users',
      tags: ['user'],
    },
  }, async (req, res) => {
    const users = await userService.getall();
    res.send(users);
  });

  app.get('/:id', {
    schema: {
      description: 'Get user by id',
      tags: ['user'],
      params: {
        type: 'object',
        properties: {
          id: { type: 'string', format: 'uuid' },
        },
      },
    },
  }, async (req: FastifyRequest<{Params: {id: string}}>, res) => {
    const { id } = req.params;

    try {
      const user = await userService.get(id);
      if (!user) res.code(404).send('User not found');
      res.send(user);
    } catch (e) {
      res.code(400).send('Bad request from user');
    }
  });
};

export default routes;
