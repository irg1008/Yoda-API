import type { Consts, FineTuneConfig } from './openai.types';

export const fineTuneConfig: FineTuneConfig = {
  model: 'curie',
  batchSize: 4,
  iters: 10,
  modelName: 'shortener-v0-1',
};

const TIME_MARK = '2022-06-08-08-04-32';
const trainedModel = `${
  fineTuneConfig.model
}:ft-personal:${fineTuneConfig.modelName.toLowerCase()}-${TIME_MARK}`;

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
