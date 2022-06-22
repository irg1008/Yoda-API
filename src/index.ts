import Fastify from 'fastify';
import { userRoutes } from 'routes';
import { fastifyOptions } from 'config/fastify';

const app = Fastify(fastifyOptions);

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.register(userRoutes, { prefix: '/user' });

app.listen({ port: 3000 });
