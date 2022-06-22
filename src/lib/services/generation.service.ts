import { hash } from 'lib/utils/crypto';
import { db } from 'lib/db';
import type { GenerationData } from 'lib/db/models';

const logGeneration = (generationData: GenerationData) => {
  const hashedInput = hash(generationData.input);

  return db.generation.create({
    data: {
      ...generationData,
      hash: hashedInput,
    },
  });
};

const getGeneration = (prompt: string) => {
  const hadhedInput = hash(prompt);
  return db.generation.findUnique({ where: { hash: hadhedInput } });
};

export default {
  logGeneration,
  getGeneration,
};
