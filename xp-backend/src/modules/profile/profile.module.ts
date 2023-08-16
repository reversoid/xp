import { Module } from '@nestjs/common';
import { ProfileController } from './profile.controller';
import { ProfileService } from './profile.service';
import { ObservationModule } from '../observation/observation.module';
import { ExperimentModule } from '../experiment/experiment.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Subscription } from './entities/Subscription';

@Module({
  controllers: [ProfileController],
  providers: [ProfileService],
  imports: [
    ObservationModule,
    ExperimentModule,
    TypeOrmModule.forFeature([Subscription]),
  ],
})
export class ProfileModule {}
