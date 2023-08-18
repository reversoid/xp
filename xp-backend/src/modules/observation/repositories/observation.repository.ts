import { DataSource, LessThanOrEqual } from 'typeorm';
import { Observation } from '../entities/observation.entity';
import { Injectable } from '@nestjs/common';
import { DateTime } from 'luxon';
import { PaginatedRepository } from 'src/shared/paginated.repository';

@Injectable()
export class ObservationRepository extends PaginatedRepository<Observation> {
  constructor(dataSource: DataSource) {
    super(Observation, dataSource.createEntityManager());
  }

  async getRandomObservations(amount: number, userIdToIgnore?: number) {
    const query = super
      .createQueryBuilder('observation')
      .select('observation')
      .addSelect('RANDOM()', 'random')
      .leftJoin('observation.user', 'user')
      .orderBy('random')
      .take(amount);

    if (userIdToIgnore !== undefined) {
      query.where('user.id != :userIdToIgnore', { userIdToIgnore });
    }

    return query.getMany();
  }

  async getUserObservations(userId: number, limit = 10, lowerBound?: DateTime) {
    const observations = await this.find({
      where: {
        user: { id: userId },
        created_at: lowerBound && LessThanOrEqual(lowerBound),
      },
      order: { created_at: 'DESC' },
      take: limit + 1,
    });
    return this.processPaginationByCreatedDate(observations, limit);
  }
}
