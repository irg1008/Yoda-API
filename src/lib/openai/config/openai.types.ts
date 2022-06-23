export const models = ['ada', 'babbage', 'curie', 'davinci'] as const;
export type ModelName = typeof models[number];

export interface FineTuneConfig {
  model: ModelName;
  batchSize: number;
  iters: number;
  modelName: string;
}

export interface Consts {
  /**
   * Name of the fine-tune model. Base models can be used as well.
   *
   * @type {string}
   * @memberof Consts
   */
  fineTunnedModel: string;

  /**
   * Max number of chars in a prompt.
   *
   * @type {number}
   * @memberof Consts
   */
  maxPromptLength: number;

  /**
   * Min tokens to use. Use this for control on maxTokenDownSample. Set to 0 for no control.
   *
   * @type {number}
   * @memberof Consts
   */
  minTokens: number;

  /**
   * Max number of tokens in a prompt. Approx. 65 chars.
   *
   * @type {number}
   * @memberof Consts
   */
  maxTokens: number;

  /**
   * Max tokens downsample. i.e: Input is 22 tokens so we set the
   * max to floored 22 * 0.7 = 15. Never go above maxTokens.
   * Set to one if you always want to use maxTokens value.
   *
   * @type {number}
   * @memberof Consts
   */
  maxTokenDownSample: number;

  /**
   * Start of prompt.
   *
   * @type {string}
   * @memberof Consts
   */
  promptStart: string;

  /**
   * End separator for prompt.
   *
   * @type {string}
   * @memberof Consts
   */
  promptEnd: string;

  /**
   * Start of completion.
   *
   * @type {string}
   * @memberof Consts
   */
  completionStart: string;

  /**
   * End separator for completion.
   *
   * @type {string}
   * @memberof Consts
   */
  completionEnd: string;
}
