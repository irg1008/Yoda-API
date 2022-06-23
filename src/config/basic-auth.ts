import { FastifyBasicAuthOptions } from '@fastify/basic-auth';

export const basicAuthOptions: FastifyBasicAuthOptions = {
  validate: async (username, password, req, reply, done) => {
    if (username === 'admin' && password === 'admin') {
      done();
    } else {
      done(new Error('Invalid credentials'));
    }
  },
  authenticate: true,
};
