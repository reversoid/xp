import Sqids from "sqids";

const squids = new Sqids({ minLength: 10 });

export const encodeCursor = (cursor: number) => {
  return squids.encode([cursor]);
};

export const decodeCursor = (key: string) => {
  return squids.decode(key)[0] ?? 1;
};
