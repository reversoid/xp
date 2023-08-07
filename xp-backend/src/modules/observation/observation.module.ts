import { Module } from '@nestjs/common';
import { ObservationController } from './observation.controller';
import { ObservationService } from './observation.service';

@Module({
  controllers: [ObservationController],
  providers: [ObservationService],
})
export class ObservationModule {}
