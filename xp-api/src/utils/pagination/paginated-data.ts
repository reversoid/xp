export type PaginatedData<T = unknown> = {
  items: T[];
  cursor: string | null;
};
