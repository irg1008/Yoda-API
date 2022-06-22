import { encode as gpt3Encode } from 'gpt-3-encoder';
import { decode } from './decoder';

export const encode = (str: string) => {
  const encoded = gpt3Encode(str);
  const encodedStrs = encoded.map((token) => decode([token]));
  const nTokens = encoded.length;
  return { encoded, encodedStrs, nTokens };
};
