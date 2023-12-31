import { Injectable } from '@nestjs/common';
import { DataSource, LessThanOrEqual } from 'typeorm';
import { Experiment, ExperimentStatus } from '../entities/experiment.entity';
import { DateTime } from 'luxon';
import {
  PaginatedRepository,
  PaginatedResponse,
} from 'src/shared/paginated.repository';
import { ExperimentView } from '../entities/experiment-view.entity';
import { Subscription } from 'src/modules/user/entities/Subscription.entity';

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
        completed_at:
          lower_bound && LessThanOrEqual(lower_bound.plus({ millisecond: 1 })),
      },
      order: { completed_at: 'DESC' },
      take: limit + 1,
      relations: { observations: true },
    });

    return this.processPaginationByCompletedDate(experiments, limit);
  }

  /** Returns random unseen experiments from users not followed by you and ignoring your experiments */
  async getRandomUnseenExperiments(userId: number, limit: number) {
    return this.createQueryBuilder('experiment')
      .leftJoinAndSelect('experiment.user', 'experimentUser')
      .leftJoin(
        ExperimentView,
        'experimentView',
        'experiment.id = experimentView.experimentId AND experimentView.user.id = :userId',
        { userId },
      )
      .leftJoin(
        Subscription,
        'subscription',
        'experimentUser.id = subscription.followed.id AND subscription.follower.id = :userId',
        { userId },
      )
      .addSelect('RANDOM()', 'random')
      .where('experimentView.id IS NULL')
      .andWhere('subscription.id IS NULL')
      .andWhere('experimentUser.id != :userId', { userId })
      .orderBy('random')
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
    let next_key: DateTime | null = null;
    if (items.length > limit) {
      const lastItem = items.at(limit);
      next_key = lastItem.completed_at;
    }
    return { items: items.slice(0, limit), next_key };
  }
}
