import { FastifyPluginAsync } from 'fastify';
import { userService } from 'lib/services';

const routes: FastifyPluginAsync = async (app, opts) => {
  app.get('/', async (req, res) => {
    const users = userService.getall();
    res.send(users);
  });
};

export default routes;
