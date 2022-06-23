import { FastifyBearerAuthOptions } from '@fastify/bearer-auth';
import { apiKeyService } from 'lib/services';

const listApiKeys = async () => {
  const apiKeys = await apiKeyService.list();
  return new Set(apiKeys.map((apiKey) => apiKey.apiKey));
};

export const getBearerAuthOptions = async (): Promise<FastifyBearerAuthOptions> => {
  const apiKeys = await listApiKeys();
  return { keys: apiKeys };
};
