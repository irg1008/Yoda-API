import type { ModelName } from '../openai.types';

interface TrainingUsagePrices {
  training: number;
  usage: number;
}

// Prices is in $/1000 tokens:
export const prices: Record<ModelName, TrainingUsagePrices> = {
  ada: {
    training: 0.0004,
    usage: 0.0016,
  },
  babbage: {
    training: 0.0006,
    usage: 0.0024,
  },
  curie: {
    training: 0.003,
    usage: 0.012,
  },
  davinci: {
    training: 0.03,
    usage: 0.12,
  },
};
