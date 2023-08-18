import { Injectable } from '@nestjs/common';
import { DataSource, LessThanOrEqual } from 'typeorm';
import { Experiment, ExperimentStatus } from '../entities/experiment.entity';
import { DateTime } from 'luxon';
import {
  PaginatedRepository,
  PaginatedResponse,
} from 'src/shared/paginated.repository';
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

    return this.processPaginationByCreatedDate(experiments, limit);
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

  async getLatestExperimentsFromFollowee(userId: number, limit: number) {
    const experiments = await this.createQueryBuilder('experiment')
      .innerJoin(
        Subscription,
        'subscription',
        'experiment.userId = subscription.followed_id AND subscription.follower_id = :userId',
        { userId },
      )
      .leftJoin(
        ExperimentView,
        'experimentView',
        'experiment.id = experimentView.experimentId AND experimentView.userId = :userId',
        { userId },
      )
      .where('experiment.completed_at IS NOT NULL')
      .andWhere('experimentView.id IS NULL')
      .orderBy('experiment.completed_at', 'DESC')
      .take(limit + 1)
      .getMany();

    return this.processPaginationByCompletedDate(experiments, limit);
  }

  private processPaginationByCompletedDate<
    V extends { completed_at: DateTime },
  >(items: V[], limit: number): PaginatedResponse<V> {
    let next_key = null;
    if (items.length > limit) {
      const lastItem = items.at(limit);
      next_key = lastItem.completed_at;
    }
    return { items: items.slice(0, limit), next_key };
  }
}
