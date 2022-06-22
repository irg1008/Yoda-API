import { FastifyServerOptions } from 'fastify';

export const fastifyOptions: Pick<FastifyServerOptions, 'logger'> = {
  logger:
    {
      transport: {
        target: 'pino-pretty',
        options: {
          translateTime: 'SYS:HH:MM:ss',
          ignore: 'reqId,req.hostname,req.remoteAddress,req.remotePort',
          singleLine: true,
          levelFirst: true,
        },
      },
    },
};
