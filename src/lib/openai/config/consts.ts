import type { Consts, FineTuneConfig } from './openai.types';

export const fineTuneConfig: FineTuneConfig = {
  model: 'curie',
  batchSize: 4,
  iters: 10,
  modelName: 'shortener-v0-2',
};

const TIME_MARK = '2022-07-27-10-54-50'; // Change this when creating new model.
const trainedModel = `${
  fineTuneConfig.model
}:ft-lighthouse-feed:${fineTuneConfig.modelName.toLowerCase()}-${TIME_MARK}`;

export const consts: Consts = {
  fineTunnedModel: trainedModel,
  maxPromptLength: 150,
  minTokens: 15,
  maxTokens: 22,
  maxTokenDownSample: 0.7,
  promptStart: 'Long: ',
  promptEnd: '',
  completionStart: 'Short: ',
  completionEnd: '.',
};
