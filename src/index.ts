import Fastify from 'fastify';
import { routes } from 'routes';
import { fastifyOptions } from 'config/fastify';
import { addDocs } from 'lib/utils/docs';

const startApp = async () => {
  const app = Fastify(fastifyOptions);

  await addDocs(app, { prefix: '/docs' });
  app.register(routes, { prefix: '/api' });

  await app.ready();
  app.swagger();
  app.listen({ port: 5050, host: '0.0.0.0' });
};

startApp();
