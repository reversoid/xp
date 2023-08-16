import { DateTime } from 'luxon';
import { Repository } from 'typeorm';

export class PaginatedResponse<T> {
  items: T[];
  next_key: DateTime | null;
}

export class PaginatedRepository<
  T extends { created_at: DateTime },
> extends Repository<T> {
  processPagination<V extends { created_at: DateTime } = T>(
    items: V[],
    limit: number,
  ): PaginatedResponse<V> {
    let next_key = null;
    if (items.length > limit) {
      const lastItem = items.at(limit);
      next_key = lastItem.created_at;
    }
    return { items: items.slice(0, limit), next_key };
  }
}
