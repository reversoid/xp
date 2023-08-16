import { Module } from '@nestjs/common';
import { ProfileController } from './profile.controller';
import { ProfileService } from './profile.service';
import { ObservationModule } from '../observation/observation.module';
import { ExperimentModule } from '../experiment/experiment.module';

@Module({
  controllers: [ProfileController],
  providers: [ProfileService],
  imports: [ObservationModule, ExperimentModule],
})
export class ProfileModule {}
