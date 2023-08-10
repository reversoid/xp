import { Module } from '@nestjs/common';
import { ScheduleModule } from '@nestjs/schedule';
import { ValidateExperimentsService } from './services/validate-experiments.service';
import { ExperimentModule } from '../experiment/experiment.module';

@Module({
  imports: [ScheduleModule.forRoot(), ExperimentModule],
  providers: [ValidateExperimentsService],
})
export class TaskModule {}
