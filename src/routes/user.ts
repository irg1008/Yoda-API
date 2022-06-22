import { FastifyPluginAsync, FastifyRequest } from 'fastify';
import { userService } from 'lib/services';

const routes: FastifyPluginAsync = async (app, opts) => {
  app.get('/', async (req, res) => {
    const users = await userService.getall();
    res.send(users);
  });

  app.get('/:id', async (req: FastifyRequest<{Params: {id: string}}>, res) => {
    const { id } = req.params;

    try {
      const user = await userService.get(id);
      console.log(user);
      if (!user) res.code(404).send('User not found');
      res.send(user);
    } catch (e) {
      res.code(400).send('Bad request from user');
    }
  });
};

export default routes;
