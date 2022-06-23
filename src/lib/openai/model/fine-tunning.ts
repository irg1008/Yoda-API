import type { FineTuneConfig } from '../config/openai.types';
import { withError } from '../utils/error-handler';
import { openai } from './api';

export const listFineTunes = async () => {
  const { data, error } = await withError(() => openai.listFineTunes());
  return {
    data: data?.data,
    error,
  };
};

export const createFineTune = (
  fileId: string,
  {
    batchSize, model, modelName, iters,
  }: FineTuneConfig,
) => withError(() => openai.createFineTune({
  training_file: fileId,
  model,
  batch_size: batchSize,
  suffix: modelName,
  n_epochs: iters,
}));
