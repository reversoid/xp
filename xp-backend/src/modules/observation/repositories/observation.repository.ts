import { DataSource, LessThanOrEqual } from 'typeorm';
import { Observation } from '../entities/observation.entity';
import { Injectable } from '@nestjs/common';
import { DateTime } from 'luxon';
import { PaginatedRepository } from 'src/shared/paginated.repository';
import { ObservationView } from '../entities/observation-view.entity';

@Injectable()
export class ObservationRepository extends PaginatedRepository<Observation> {
  constructor(dataSource: DataSource) {
    super(Observation, dataSource.createEntityManager());
  }

  async getRandomObservations(amount: number, forUserId: number) {
    const query = super
      .createQueryBuilder('observation')
      .leftJoin(
        ObservationView,
        'observationView',
        'experiment.id = observationView.experimentId AND observationView.userId = :userId',
        { userId: forUserId },
      )
      .leftJoin('observation.user', 'user')
      .select('observation')
      .addSelect('RANDOM()', 'random')
      .where('observationView.id IS NULL')
      .andWhere('user.id != :userId', { userId: forUserId })
      .orderBy('random')
      .take(amount);

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
