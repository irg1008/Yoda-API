import { consts } from 'lib/openai/config/consts';
import { getCompletion as getOpenAICompletion } from 'lib/openai/model/completions';
import type { WithError } from 'lib/openai/utils/error-handler';
import type { Completion } from 'lib/db/models';

const getCompletion = async (
  prompt: string,
): Promise<WithError<Completion>> => {
  const { data, error } = await getOpenAICompletion(
    consts.fineTunnedModel,
    prompt,
  );
  if (error) return { error, data: null };

  const completion = data?.choices?.[0]?.text?.replace(consts.completionStart, '') ?? '';
  return { error, data: { completion } };
};

export default {
  getCompletion,
};
