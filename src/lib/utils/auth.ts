import bearerAuth from '@fastify/bearer-auth';
import { getBearerAuthOptions } from 'config/bearer-auth';
import { FastifyInstance } from 'fastify';

export const authApp = async (app: FastifyInstance) => {
  const bearerAuthOptions = await getBearerAuthOptions();
  app.register(bearerAuth, bearerAuthOptions);
};
