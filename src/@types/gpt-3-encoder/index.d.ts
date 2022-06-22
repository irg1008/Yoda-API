declare module 'gpt-3-encoder' {
  export const encode: (str: string) => number[];
  export const decode: (tokens: number[]) => string;
}
