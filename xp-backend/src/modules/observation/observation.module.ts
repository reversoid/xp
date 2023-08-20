import { Module } from '@nestjs/common';
import { ObservationController } from './observation.controller';
import { ObservationService } from './observation.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Observation } from './entities/observation.entity';
import { ObservationRepository } from './repositories/observation.repository';
import { UserModule } from '../user/user.module';
import { ObservationView } from './entities/observation-view.entity';
import { ObservationViewRepository } from './repositories/observation-view.repository';

@Module({
  imports: [
    TypeOrmModule.forFeature([Observation, ObservationView]),
    UserModule,
  ],
  controllers: [ObservationController],
  providers: [
    ObservationService,
    ObservationRepository,
    ObservationViewRepository,
  ],
  exports: [ObservationRepository],
})
export class ObservationModule {}
