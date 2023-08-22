import { Module } from '@nestjs/common';
import { ProfileController } from './profile.controller';
import { ProfileService } from './profile.service';
import { ObservationModule } from '../observation/observation.module';
import { ExperimentModule } from '../experiment/experiment.module';
import { UserModule } from '../user/user.module';

@Module({
  imports: [ObservationModule, ExperimentModule, UserModule],
  controllers: [ProfileController],
  providers: [ProfileService],
})
export class ProfileModule {}
