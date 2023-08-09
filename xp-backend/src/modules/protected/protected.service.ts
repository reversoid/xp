import { Injectable } from '@nestjs/common';
import { DateTime } from 'luxon';
import {
  Experiment,
  ExperimentStatus,
} from '../experiment/entities/experiment.entity';
import { ExperimentRepository } from '../experiment/repository/experiment.repository';

@Injectable()
export class ProtectedService {
  constructor(private experimentRepository: ExperimentRepository) {}

  async getAllUnfinishedExperiments(): Promise<Experiment[]> {
    const experiments = await this.experimentRepository
      .createQueryBuilder('experiment')
      .select([
        'experiment.complete_by',
        'experiment.id',
        'experiment.status',
        'experiment.created_at',
      ])
      .addSelect('user.id', 'userId')
      .leftJoin('experiment.user', 'user')
      .where('experiment.complete_by > :completeBy', {
        completeBy: DateTime.now().toJSDate(),
      })
      .andWhere('experiment.status = :status', {
        status: ExperimentStatus.STARTED,
      })
      .getMany();

    return experiments;
  }
}
