import { Module } from '@nestjs/common';
import { ObservationController } from './observation.controller';
import { ObservationService } from './observation.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Observation } from './entities/observation.entity';
import { ObservationRepository } from './repositories/observation.repository';
import { UserModule } from '../user/user.module';

@Module({
  imports: [TypeOrmModule.forFeature([Observation]), UserModule],
  controllers: [ObservationController],
  providers: [ObservationService, ObservationRepository],
  exports: [ObservationRepository],
})
export class ObservationModule {}
