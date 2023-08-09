import { Injectable } from '@nestjs/common';
import { ExperimentRepository } from '../experiment/repository/experiment.repository';
import { MoreThan } from 'typeorm';
import { DateTime } from 'luxon';
import {
  Experiment,
  ExperimentStatus,
} from '../experiment/entities/experiment.entity';

@Injectable()
export class ProtectedService {
  constructor(private experimentRepository: ExperimentRepository) {}

  async getAllUnfinishedExperiments(): Promise<Experiment[]> {
    const experiments = await this.experimentRepository.find({
      where: {
        completed_at: MoreThan(DateTime.now().toJSDate()),
        status: ExperimentStatus.STARTED,
      },
    });

    return experiments;
  }
}
