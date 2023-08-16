import { Module } from '@nestjs/common';
import { ExperimentController } from './experiment.controller';
import { ExperimentService } from './experiment.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Experiment } from './entities/experiment.entity';
import { ExperimentRepository } from './repository/experiment.repository';
import { UserModule } from '../user/user.module';
import { ExperimentView } from './entities/experiment-view.entity';

@Module({
  imports: [UserModule, TypeOrmModule.forFeature([Experiment, ExperimentView])],
  controllers: [ExperimentController],
  providers: [ExperimentService, ExperimentRepository],
  exports: [ExperimentRepository],
})
export class ExperimentModule {}
