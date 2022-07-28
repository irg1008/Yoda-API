import Fastify from 'fastify';
import { routes } from 'routes';
import { fastifyOptions } from 'config/fastify';
import { addDocs } from 'lib/utils/docs';

const startApp = async () => {
  const app = Fastify(fastifyOptions);

  await addDocs(app, { prefix: '/docs' });
  app.register(routes, { prefix: '/api' });

  app.get(
    '/',
    {
      schema: { hide: true },
    },
    async (_, reply) => {
      reply.send({ hello: 'Yoda FITS (First Intergalactic Title Shortener)' });
    },
  );

  await app.ready();
  app.swagger();

  const envPort = process.env.PORT;
  const port = envPort ? parseInt(envPort, 10) : 3000;
  app.listen({ port, host: '0.0.0.0' });
};

startApp();
