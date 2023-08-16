import { Injectable } from '@nestjs/common';
import { DataSource, LessThanOrEqual } from 'typeorm';
import { Experiment, ExperimentStatus } from '../entities/experiment.entity';
import { DateTime } from 'luxon';
import { PaginatedRepository } from 'src/shared/paginated.repository';

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
}
