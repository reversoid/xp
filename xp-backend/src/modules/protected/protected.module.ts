import { Module } from '@nestjs/common';
import { ProtectedService } from './protected.service';
import { ProtectedController } from './protected.controller';
import { ExperimentModule } from '../experiment/experiment.module';

/** This module provides actions to perform with secret_key */
@Module({
  providers: [ProtectedService],
  controllers: [ProtectedController],
  exports: [ProtectedService],
  imports: [ExperimentModule],
})
export class ProtectedModule {}
