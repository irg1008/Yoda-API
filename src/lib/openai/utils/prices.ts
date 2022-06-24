import { consts, fineTuneConfig } from '../config/consts';
import { priceOfString } from '../config/prices/prices-per-string';

export const getEstimatedPrice = (input: string, output: string) => {
  const prompt = `${consts.promptStart}${input}${consts.promptEnd}`;
  const completion = `${consts.completionStart}${output}${consts.completionEnd}`;

  const { usagePrice: promptPrice } = priceOfString(prompt, fineTuneConfig.model);
  const { usagePrice: completionPrice } = priceOfString(completion, fineTuneConfig.model);

  return promptPrice + completionPrice;
};
