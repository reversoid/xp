import { Module } from '@nestjs/common';
import { ProfileController } from './profile.controller';
import { ProfileService } from './profile.service';
import { ObservationModule } from '../observation/observation.module';
import { ExperimentModule } from '../experiment/experiment.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Subscription } from './entities/Subscription';
import { SubscriptionRepository } from './repositories/subscription.repository';
import { UserModule } from '../user/user.module';

@Module({
  controllers: [ProfileController],
  providers: [ProfileService, SubscriptionRepository],
  imports: [
    ObservationModule,
    ExperimentModule,
    UserModule,
    TypeOrmModule.forFeature([Subscription]),
  ],
})
export class ProfileModule {}
