import type { CreateCompletionRequest, CreateCompletionResponse } from 'openai';
import { openai } from './api';
import { withError } from '../utils/error-handler';
import type { WithError } from '../utils/error-handler';
import { consts } from '../config/consts';
import { encode } from '../encoder';

const getMaxTokensForPrompt = (userPrompt: string) => {
  const finalPrompt = userPrompt + consts.promptEnd;
  const { nTokens } = encode(finalPrompt);
  const tokenDownSample = Math.floor(nTokens * consts.maxTokenDownSample);
  const maxOutTokens = Math.max(
    Math.min(consts.maxTokens, tokenDownSample),
    consts.minTokens,
  );
  return maxOutTokens;
};

export const getCompletion = (
  model: string,
  userPrompt: string,
  options?: CreateCompletionRequest,
): Promise<WithError<CreateCompletionResponse>> => {
  const maxOutTokens = getMaxTokensForPrompt(userPrompt);

  return withError(() => openai.createCompletion({
    model,
    prompt: `${consts.promptStart}${userPrompt}${consts.promptEnd}`,
    echo: false,
    stop: consts.completionEnd,
    max_tokens: maxOutTokens,
    temperature: 0.2,
    top_p: 0.5,
    ...options,
  }));
};
