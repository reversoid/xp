import { Injectable } from '@nestjs/common';
import { Cron } from '@nestjs/schedule';
import { InjectRepository } from '@nestjs/typeorm';
import { ExperimentRepository } from 'src/modules/experiment/repository/experiment.repository';
import { ExperimentStatus } from 'src/modules/experiment/entities/experiment.entity';
import { DateTime } from 'luxon';
import { TWICE_A_DAY } from '../cron.constants';

@Injectable()
export class ValidateExperimentsService {
  constructor(
    @InjectRepository(ExperimentRepository)
    private readonly experimentRepository: ExperimentRepository,
  ) {}

  @Cron(TWICE_A_DAY)
  async cancelExpiredExperiments() {
    await this.experimentRepository
      .createQueryBuilder('experiment')
      .update({ status: ExperimentStatus.CANCELED })
      .where('experiment.complete_by <= :date', { date: DateTime.now() })
      .execute();
  }
}
