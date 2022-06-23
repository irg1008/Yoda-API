import basicAuth from '@fastify/basic-auth';
import { basicAuthOptions } from 'config/basic-auth';
import { swaggerOptions } from 'config/swagger';
import { FastifyInstance } from 'fastify';
import swagger from '@fastify/swagger';

export const addDocs = async (app: FastifyInstance, { prefix }: {prefix: string}) => {
  await app.register(basicAuth, basicAuthOptions);
  app.register(swagger, {
    ...swaggerOptions,
    uiHooks: { onRequest: app.basicAuth },
    routePrefix: prefix,
  });
};
