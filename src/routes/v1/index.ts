import { FastifyPluginAsync } from 'fastify';
import userRoutes from './user';
import completionRoutes from './completion';

const routes: FastifyPluginAsync = async (app) => {
  app.get('/', async (_, res) => {
    res.send({ version: 'v1' });
  });

  app.register(userRoutes, { prefix: '/user' });
  app.register(completionRoutes, { prefix: '/completion' });
};

export { routes };
