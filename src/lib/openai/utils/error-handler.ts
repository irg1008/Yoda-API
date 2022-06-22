import type { AxiosResponse } from 'axios';

export interface WithError<T = unknown> {
  data: T | null;
  error: Error | null;
}

export const withError = async <T>(
  fn: () => Promise<AxiosResponse<T>>
): Promise<WithError<T>> => {
  try {
    const { data } = await fn();
    return { data, error: null };
  } catch (err) {
    const error = err as Error;
    return { data: null, error };
  }
};
