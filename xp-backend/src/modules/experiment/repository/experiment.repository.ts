import { Injectable } from '@nestjs/common';
import { DataSource, LessThanOrEqual } from 'typeorm';
import { Experiment, ExperimentStatus } from '../entities/experiment.entity';
import { DateTime } from 'luxon';
import { PaginatedRepository } from 'src/shared/paginated.repository';
import { ExperimentView } from '../entities/experiment-view.entity';
import { Subscription } from 'src/modules/profile/entities/Subscription';

@Injectable()
export class ExperimentRepository extends PaginatedRepository<Experiment> {
  constructor(dataSource: DataSource) {
    super(Experiment, dataSource.createEntityManager());
  }

  async getUserCompletedExperiments(
    userId: number,
    limit = 10,
    lower_bound?: DateTime,
  ) {
    const experiments = await this.find({
      where: {
        user: { id: userId },
        status: ExperimentStatus.COMPLETED,
        completed_at: lower_bound && LessThanOrEqual(lower_bound),
      },
      order: { completed_at: 'DESC' },
      take: limit + 1,
      relations: { observations: true },
    });

    return this.processPagination(experiments, limit);
  }

  async getRandomUnseenExperiments(userId: number, limit: number) {
    return this.createQueryBuilder('experiment')
      .leftJoin(
        ExperimentView,
        'experimentView',
        'experiment.id = experimentView.experimentId AND experimentView.userId = :userId',
        { userId },
      )
      .leftJoin(
        Subscription,
        'subscription',
        'experiment.userId = subscription.followed_id AND subscription.follower_id = :userId',
        { userId },
      )
      .where('experimentView.id IS NULL')
      .andWhere('subscription.id IS NULL')
      .orderBy('RANDOM()')
      .take(limit)
      .getMany();
  }
}
