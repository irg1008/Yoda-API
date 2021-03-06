import { SwaggerOptions } from '@fastify/swagger';

export const swaggerOptions: SwaggerOptions = {
  swagger: {
    info: {
      title: 'Yoda API',
      description: 'Title summarization and description keyword extraction',
      version: '0.2.0',
    },
    externalDocs: {
      url: 'https://github.com/irg1008/Yoda-API.git',
      description: 'Find more info here',
    },
    tags: [{ name: 'user', description: 'User related end-points' }],
    definitions: {
      // User: {
      //   type: 'object',
      //   required: ['id', 'email'],
      //   properties: {
      //     id: { type: 'string', format: 'uuid' },
      //     firstName: { type: 'string' },
      //     lastName: { type: 'string' },
      //     email: { type: 'string', format: 'email' },
      //   },
      // },
    },
    securityDefinitions: {
      apiKey: {
        type: 'apiKey',
        name: 'apiKey',
        in: 'header',
      },
    },
  },
  uiConfig: {
    docExpansion: 'list',
  },
  exposeRoute: true,
};
