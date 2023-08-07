import { Module } from '@nestjs/common';
import { ProtectedService } from './protected.service';
import { ProtectedController } from './protected.controller';

/** This module provides actions to perform with secret_key */
@Module({
  providers: [ProtectedService],
  controllers: [ProtectedController],
  exports: [ProtectedService],
})
export class ProtectedModule {}
