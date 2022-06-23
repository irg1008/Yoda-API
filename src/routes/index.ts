import { FastifyPluginAsync } from 'fastify';
import { routes as v1 } from './v1';

export const routes: FastifyPluginAsync = async (app) => {
  app.register(v1, { prefix: '/v1' });
};
