import Fastify from 'fastify';

const app = Fastify({
  logger: true,
});

app.get('/', async (req, res) => {
  res.send({ hello: 'world' });
});

app.listen({ port: 3000 }, (err, address) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(`server listening on ${address}`);
});
