import { Module } from '@nestjs/common';
import { ExperimentController } from './experiment.controller';
import { ExperimentService } from './experiment.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Experiment } from './entities/experiment.entity';

@Module({
  imports: [TypeOrmModule.forFeature([Experiment])],
  controllers: [ExperimentController],
  providers: [ExperimentService],
})
export class ExperimentModule {}
