import { Module } from '@nestjs/common';
import { ExperimentController } from './experiment.controller';
import { ExperimentService } from './experiment.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Experiment } from './entities/experiment.entity';
import { ExperimentRepository } from './repository/experiment.repository';
import { UserModule } from '../user/user.module';

@Module({
  imports: [UserModule, TypeOrmModule.forFeature([Experiment])],
  controllers: [ExperimentController],
  providers: [ExperimentService, ExperimentRepository],
  exports: [ExperimentRepository],
})
export class ExperimentModule {}
