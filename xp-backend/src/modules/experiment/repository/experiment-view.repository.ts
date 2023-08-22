import { Injectable } from '@nestjs/common';
import { DataSource, DeepPartial, MoreThan, Repository } from 'typeorm';
import { ExperimentView } from '../entities/experiment-view.entity';
import { DateTime } from 'luxon';

@Injectable()
export class ExperimentViewRepository extends Repository<ExperimentView> {
  constructor(dataSource: DataSource) {
    super(ExperimentView, dataSource.createEntityManager());
  }

  async markExperimentAsViewed(userId: number, experimentId: number) {
    return this.save({
      experiment: { id: experimentId },
      user: { id: userId },
    });
  }

  async markManyExperimentsAsViewed(userId: number, experimentsIds: number[]) {
    return this.save(
      experimentsIds.map<DeepPartial<ExperimentView>>((id) => ({
        user: { id: userId },
        experiment: { id },
      })),
    );
  }

  async isExperimentViewed(userId: number, experimentId: number) {
    return this.findOneBy({
      experiment: { id: experimentId },
      user: { id: userId },
    });
  }

  async seenLastWeek(userId: number) {
    const lastWeekDate = DateTime.now().minus({ days: 7 });

    return this.count({
      where: {
        seen_at: MoreThan(lastWeekDate),
        user: {
          id: userId,
        },
      },
    });
  }
}
